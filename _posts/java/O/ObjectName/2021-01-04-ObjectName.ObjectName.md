---
title: ObjectName.ObjectName()
permalink: Java/ObjectName/ObjectName
date: 2021-01-04
key: JavaJava.O.ObjectName
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectName.constructores valor="ObjectName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ObjectName(String name) throws MalformedObjectNameException
public ObjectName(String domain, String key, String value) throws MalformedObjectNameException
public ObjectName(String domain, Hashtable<String,String> table) throws MalformedObjectNameException
~~~

## Parámetros
* **String&gt; table**,  {% include w3api/param_description.html metodo=_data parametro="String> table" %}
* **String value**,  {% include w3api/param_description.html metodo=_data parametro="String value" %}
* **Hashtable&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Hashtable<String" %}
* **String domain**,  {% include w3api/param_description.html metodo=_data parametro="String domain" %}
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

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
{%- for _ldc in site.data.Java.O.ObjectName.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
