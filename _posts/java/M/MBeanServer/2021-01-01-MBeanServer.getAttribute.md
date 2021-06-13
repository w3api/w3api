---
title: MBeanServer.getAttribute()
permalink: Java/MBeanServer/getAttribute
date: 2021-01-11
key: JavaJava.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="getAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getAttribute(ObjectName name, String attribute) throws MBeanException, AttributeNotFoundException, InstanceNotFoundException, ReflectionException
~~~

## Parámetros
* **String attribute**,  {% include w3api/param_description.html metodo=_dato parametro="String attribute" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [ReflectionException](/Java/ReflectionException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

## Clase Padre
[MBeanServer](/Java/MBeanServer/)

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
