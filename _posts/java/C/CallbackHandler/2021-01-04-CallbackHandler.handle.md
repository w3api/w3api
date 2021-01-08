---
title: CallbackHandler.handle()
permalink: Java/CallbackHandler/handle
date: 2021-01-04
key: JavaJava.C.CallbackHandler
category: java
tags: ['java se', 'javax.security.auth.callback', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallbackHandler.metodos valor="handle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException
~~~

## Parámetros
* **Callback[] callbacks**,  {% include w3api/param_description.html metodo=_data parametro="Callback[] callbacks" %}

## Excepciones
[UnsupportedCallbackException](/Java/UnsupportedCallbackException/), [IOException](/Java/IOException/)

## Clase Padre
[CallbackHandler](/Java/CallbackHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CallbackHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
