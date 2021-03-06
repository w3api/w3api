---
title: SslRMIServerSocketFactory.SslRMIServerSocketFactory()
permalink: /Java/SslRMIServerSocketFactory/SslRMIServerSocketFactory/
date: 2021-01-11
key: Java.S.SslRMIServerSocketFactory
category: Java
tags: ['java se', 'javax.rmi.ssl', 'java.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SslRMIServerSocketFactory.constructores valor="SslRMIServerSocketFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SslRMIServerSocketFactory()
public SslRMIServerSocketFactory(String[] enabledCipherSuites, String[] enabledProtocols, boolean needClientAuth) throws IllegalArgumentException
public SslRMIServerSocketFactory(SSLContext context, String[] enabledCipherSuites, String[] enabledProtocols, boolean needClientAuth) throws IllegalArgumentException
~~~

## Parámetros
* **SSLContext context**,  {% include w3api/param_description.html metodo=_dato parametro="SSLContext context" %}
* **String[] enabledProtocols**,  {% include w3api/param_description.html metodo=_dato parametro="String[] enabledProtocols" %}
* **String[] enabledCipherSuites**,  {% include w3api/param_description.html metodo=_dato parametro="String[] enabledCipherSuites" %}
* **boolean needClientAuth**,  {% include w3api/param_description.html metodo=_dato parametro="boolean needClientAuth" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SslRMIServerSocketFactory](/Java/SslRMIServerSocketFactory/)

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
