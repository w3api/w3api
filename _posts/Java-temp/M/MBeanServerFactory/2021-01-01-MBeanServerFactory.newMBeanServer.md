---
title: MBeanServerFactory.newMBeanServer()
permalink: /Java/MBeanServerFactory/newMBeanServer/
date: 2021-01-11
key: Java.M.MBeanServerFactory
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerFactory.metodos valor="newMBeanServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MBeanServer newMBeanServer()
public static MBeanServer newMBeanServer(String domain)
~~~

## Parámetros
* **String domain**,  {% include w3api/param_description.html metodo=_dato parametro="String domain" %}

## Excepciones
[JMRuntimeException](/Java/JMRuntimeException/), [SecurityException](/Java/SecurityException/), [ClassCastException](/Java/ClassCastException/)

## Clase Padre
[MBeanServerFactory](/Java/MBeanServerFactory/)

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
