---
title: NameCallback.NameCallback()
permalink: Java/NameCallback/NameCallback
date: 2021-01-04
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
* **String defaultName**,  {% include w3api/param_description.html metodo=_data parametro="String defaultName" %}
* **String prompt**,  {% include w3api/param_description.html metodo=_data parametro="String prompt" %}

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
{%- for _ldc in site.data.Java.N.NameCallback.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
