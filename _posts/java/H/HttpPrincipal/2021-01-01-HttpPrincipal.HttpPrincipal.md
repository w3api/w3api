---
title: HttpPrincipal.HttpPrincipal()
permalink: Java/HttpPrincipal/HttpPrincipal
date: 2021-01-11
key: JavaJava.H.HttpPrincipal
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpPrincipal.constructores valor="HttpPrincipal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HttpPrincipal(String username, String realm)
~~~

## Parámetros
* **String realm**,  {% include w3api/param_description.html metodo=_dato parametro="String realm" %}
* **String username**,  {% include w3api/param_description.html metodo=_dato parametro="String username" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HttpPrincipal](/Java/HttpPrincipal/)

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
