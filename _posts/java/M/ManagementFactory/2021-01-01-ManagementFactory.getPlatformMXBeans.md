---
title: ManagementFactory.getPlatformMXBeans()
permalink: Java/ManagementFactory/getPlatformMXBeans
date: 2021-01-11
key: JavaJava.M.ManagementFactory
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ManagementFactory.metodos valor="getPlatformMXBeans" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends PlatformManagedObject>List<T> getPlatformMXBeans(Class<T> mxbeanInterface)
static <T extends PlatformManagedObject>List<T> getPlatformMXBeans(MBeanServerConnection connection, Class<T> mxbeanInterface)
~~~

## Parámetros
* **Class&lt;T&gt; mxbeanInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> mxbeanInterface" %}
* **MBeanServerConnection connection**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServerConnection connection" %}

## Clase Padre
[ManagementFactory](/Java/ManagementFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
