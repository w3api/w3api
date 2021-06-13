---
title: MBeanServerConnection.invoke()
permalink: Java/MBeanServerConnection/invoke
date: 2021-01-11
key: JavaJava.M.MBeanServerConnection
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object invoke(ObjectName name, String operationName, Object[] params, String[] signature) throws InstanceNotFoundException, MBeanException, ReflectionException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Object[] params**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] params" %}
* **String[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="String[] signature" %}
* **String operationName**,  {% include w3api/param_description.html metodo=_dato parametro="String operationName" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [IOException](/Java/IOException/)

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
