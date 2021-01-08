---
title: MessageFormat.MessageFormat()
permalink: Java/MessageFormat/MessageFormat
date: 2021-01-04
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
* **String pattern**,  {% include w3api/param_description.html metodo=_data parametro="String pattern" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MessageFormat](/Java/MessageFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
