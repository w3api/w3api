---
title: StartTlsResponse.negotiate()
permalink: Java/StartTlsResponse/negotiate
date: 2021-01-04
key: JavaJava.S.StartTlsResponse
category: java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StartTlsResponse.metodos valor="negotiate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SSLSession negotiate() throws IOException
public abstract SSLSession negotiate(SSLSocketFactory factory) throws IOException
~~~

## Parámetros
* **SSLSocketFactory factory**,  {% include w3api/param_description.html metodo=_data parametro="SSLSocketFactory factory" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[StartTlsResponse](/Java/StartTlsResponse/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StartTlsResponse.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
