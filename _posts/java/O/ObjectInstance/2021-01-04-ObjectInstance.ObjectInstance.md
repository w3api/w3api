---
title: ObjectInstance.ObjectInstance()
permalink: Java/ObjectInstance/ObjectInstance
date: 2021-01-04
key: JavaJava.O.ObjectInstance
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInstance.constructores valor="ObjectInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ObjectInstance(String objectName, String className) throws MalformedObjectNameException
public ObjectInstance(ObjectName objectName, String className)
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **String objectName**,  {% include w3api/param_description.html metodo=_data parametro="String objectName" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName objectName" %}

## Excepciones
[MalformedObjectNameException](/Java/MalformedObjectNameException/)

## Clase Padre
[ObjectInstance](/Java/ObjectInstance/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectInstance.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
