---
title: URLConnection.addRequestProperty()
permalink: /Java/URLConnection/addRequestProperty/
date: 2021-01-11
key: Java.U.URLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="addRequestProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addRequestProperty(String key, String value)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URLConnection](/Java/URLConnection/)

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
