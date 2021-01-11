---
title: ObjectName.getInstance()
permalink: Java/ObjectName/getInstance
date: 2021-01-11
key: JavaJava.O.ObjectName
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectName.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ObjectName getInstance(String name) throws MalformedObjectNameException, NullPointerException
public static ObjectName getInstance(String domain, String key, String value) throws MalformedObjectNameException
public static ObjectName getInstance(String domain, Hashtable<String,String> table) throws MalformedObjectNameException
public static ObjectName getInstance(ObjectName name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **String domain**,  {% include w3api/param_description.html metodo=_dato parametro="String domain" %}
* **String&gt; table**,  {% include w3api/param_description.html metodo=_dato parametro="String> table" %}
* **Hashtable&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<String" %}
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[MalformedObjectNameException](/Java/MalformedObjectNameException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ObjectName](/Java/ObjectName/)

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
