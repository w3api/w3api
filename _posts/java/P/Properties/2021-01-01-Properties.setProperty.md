---
title: Properties.setProperty()
permalink: /Java/Properties/setProperty/
date: 2021-01-11
key: Java.P.Properties
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.metodos valor="setProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object setProperty(String key, String value)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}

## Clase Padre
[Properties](/Java/Properties/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
