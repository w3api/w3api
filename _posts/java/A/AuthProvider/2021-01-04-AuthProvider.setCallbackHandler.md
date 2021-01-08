---
title: AuthProvider.setCallbackHandler()
permalink: Java/AuthProvider/setCallbackHandler
date: 2021-01-04
key: JavaJava.A.AuthProvider
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AuthProvider.metodos valor="setCallbackHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setCallbackHandler(CallbackHandler handler)
~~~

## Parámetros
* **CallbackHandler handler**,  {% include w3api/param_description.html metodo=_data parametro="CallbackHandler handler" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[AuthProvider](/Java/AuthProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AuthProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
