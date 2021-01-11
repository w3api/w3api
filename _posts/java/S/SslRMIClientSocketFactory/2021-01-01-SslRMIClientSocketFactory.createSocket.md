---
title: SslRMIClientSocketFactory.createSocket()
permalink: Java/SslRMIClientSocketFactory/createSocket
date: 2021-01-11
key: JavaJava.S.SslRMIClientSocketFactory
category: java
tags: ['java se', 'javax.rmi.ssl', 'java.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SslRMIClientSocketFactory.metodos valor="createSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Socket createSocket(String host, int port) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[SslRMIClientSocketFactory](/Java/SslRMIClientSocketFactory/)

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
