---
title: PasswordCallback.PasswordCallback()
permalink: /Java/PasswordCallback/PasswordCallback/
date: 2021-01-11
key: Java.P.PasswordCallback
category: java
tags: ['java se', 'javax.security.auth.callback', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PasswordCallback.constructores valor="PasswordCallback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PasswordCallback(String prompt, boolean echoOn)
~~~

## Parámetros
* **String prompt**,  {% include w3api/param_description.html metodo=_dato parametro="String prompt" %}
* **boolean echoOn**,  {% include w3api/param_description.html metodo=_dato parametro="boolean echoOn" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PasswordCallback](/Java/PasswordCallback/)

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
