---
title: SSLContext.init()
permalink: /Java/SSLContext/init/
date: 2021-01-11
key: Java.S.SSLContext
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLContext.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void init(KeyManager[] km, TrustManager[] tm, SecureRandom random) throws KeyManagementException
~~~

## Parámetros
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}
* **TrustManager[] tm**,  {% include w3api/param_description.html metodo=_dato parametro="TrustManager[] tm" %}
* **KeyManager[] km**,  {% include w3api/param_description.html metodo=_dato parametro="KeyManager[] km" %}

## Excepciones
[KeyManagementException](/Java/KeyManagementException/)

## Clase Padre
[SSLContext](/Java/SSLContext/)

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
