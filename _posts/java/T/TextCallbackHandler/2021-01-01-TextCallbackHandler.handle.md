---
title: TextCallbackHandler.handle()
permalink: Java/TextCallbackHandler/handle
date: 2021-01-11
key: JavaJava.T.TextCallbackHandler
category: java
tags: ['java se', 'com.sun.security.auth.callback', 'jdk.security.auth', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextCallbackHandler.metodos valor="handle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException
~~~

## Parámetros
* **Callback[] callbacks**,  {% include w3api/param_description.html metodo=_dato parametro="Callback[] callbacks" %}

## Excepciones
[UnsupportedCallbackException](/Java/UnsupportedCallbackException/), [IOException](/Java/IOException/)

## Clase Padre
[TextCallbackHandler](/Java/TextCallbackHandler/)

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
