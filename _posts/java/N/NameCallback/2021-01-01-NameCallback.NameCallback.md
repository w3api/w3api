---
title: NameCallback.NameCallback()
permalink: Java/NameCallback/NameCallback
date: 2021-01-11
key: JavaJava.N.NameCallback
category: java
tags: ['java se', 'javax.security.auth.callback', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NameCallback.constructores valor="NameCallback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NameCallback(String prompt)
public NameCallback(String prompt, String defaultName)
~~~

## Parámetros
* **String prompt**,  {% include w3api/param_description.html metodo=_dato parametro="String prompt" %}
* **String defaultName**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NameCallback](/Java/NameCallback/)

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
