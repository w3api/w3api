---
title: SSLSocketFactory.createSocket()
permalink: Java/SSLSocketFactory/createSocket
date: 2021-01-04
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
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}
* **Socket s**,  {% include w3api/param_description.html metodo=_data parametro="Socket s" %}
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **boolean autoClose**,  {% include w3api/param_description.html metodo=_data parametro="boolean autoClose" %}
* **InputStream consumed**,  {% include w3api/param_description.html metodo=_data parametro="InputStream consumed" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[SSLSocketFactory](/Java/SSLSocketFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLSocketFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
