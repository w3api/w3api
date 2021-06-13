---
title: ObjectInstance.ObjectInstance()
permalink: /Java/ObjectInstance/ObjectInstance/
date: 2021-01-11
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
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName objectName" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}
* **String objectName**,  {% include w3api/param_description.html metodo=_dato parametro="String objectName" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
