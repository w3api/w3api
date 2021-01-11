---
title: MBeanServerConnection.isInstanceOf()
permalink: Java/MBeanServerConnection/isInstanceOf
date: 2021-01-11
key: JavaJava.M.MBeanServerConnection
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="isInstanceOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isInstanceOf(ObjectName name, String className) throws InstanceNotFoundException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[MBeanServerConnection](/Java/MBeanServerConnection/)

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
