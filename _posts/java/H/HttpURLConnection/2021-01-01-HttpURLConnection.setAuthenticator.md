---
title: HttpURLConnection.setAuthenticator()
permalink: Java/HttpURLConnection/setAuthenticator
date: 2021-01-11
key: JavaJava.H.HttpURLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpURLConnection.metodos valor="setAuthenticator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setAuthenticator(Authenticator auth)
~~~

## Parámetros
* **Authenticator auth**,  {% include w3api/param_description.html metodo=_dato parametro="Authenticator auth" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[HttpURLConnection](/Java/HttpURLConnection/)

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
