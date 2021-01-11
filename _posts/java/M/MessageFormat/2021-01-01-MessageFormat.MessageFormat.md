---
title: MessageFormat.MessageFormat()
permalink: Java/MessageFormat/MessageFormat
date: 2021-01-11
key: JavaJava.M.MessageFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageFormat.constructores valor="MessageFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MessageFormat(String pattern)
public MessageFormat(String pattern, Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MessageFormat](/Java/MessageFormat/)

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
