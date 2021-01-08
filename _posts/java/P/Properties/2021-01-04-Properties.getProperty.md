---
title: Properties.getProperty()
permalink: Java/Properties/getProperty
date: 2021-01-04
key: JavaJava.P.Properties
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getProperty(String key)
public String getProperty(String key, String defaultValue)
~~~

## Parámetros
* **String defaultValue**,  {% include w3api/param_description.html metodo=_data parametro="String defaultValue" %}
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}

## Clase Padre
[Properties](/Java/Properties/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Properties.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
