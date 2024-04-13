---
title: StreamHandler.setEncoding()
permalink: /Java/StreamHandler/setEncoding/
date: 2021-01-11
key: Java.S.StreamHandler
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamHandler.metodos valor="setEncoding" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setEncoding(String encoding) throws SecurityException, UnsupportedEncodingException
~~~

## Parámetros
* **String encoding**,  {% include w3api/param_description.html metodo=_dato parametro="String encoding" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[StreamHandler](/Java/StreamHandler/)

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
