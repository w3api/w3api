---
title: SSLSocketFactory.createSocket()
permalink: Java/SSLSocketFactory/createSocket
date: 2021-01-11
key: JavaJava.S.SSLSocketFactory
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSocketFactory.metodos valor="createSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Socket createSocket(Socket s, InputStream consumed, boolean autoClose) throws IOException
public abstract Socket createSocket(Socket s, String host, int port, boolean autoClose) throws IOException
~~~

## Parámetros
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **InputStream consumed**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream consumed" %}
* **Socket s**,  {% include w3api/param_description.html metodo=_dato parametro="Socket s" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **boolean autoClose**,  {% include w3api/param_description.html metodo=_dato parametro="boolean autoClose" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[SSLSocketFactory](/Java/SSLSocketFactory/)

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
