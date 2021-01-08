---
title: MBeanRegistration.preRegister()
permalink: Java/MBeanRegistration/preRegister
date: 2021-01-04
key: JavaJava.M.MBeanRegistration
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanRegistration.metodos valor="preRegister" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectName preRegister(MBeanServer server, ObjectName name) throws Exception
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}
* **MBeanServer server**,  {% include w3api/param_description.html metodo=_data parametro="MBeanServer server" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[MBeanRegistration](/Java/MBeanRegistration/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanRegistration.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
