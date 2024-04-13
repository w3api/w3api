---
title: SSLContextSpi.engineInit()
permalink: /Java/SSLContextSpi/engineInit/
date: 2021-01-11
key: Java.S.SSLContextSpi
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLContextSpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(KeyManager[] km, TrustManager[] tm, SecureRandom sr) throws KeyManagementException
~~~

## Parámetros
* **SecureRandom sr**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom sr" %}
* **TrustManager[] tm**,  {% include w3api/param_description.html metodo=_dato parametro="TrustManager[] tm" %}
* **KeyManager[] km**,  {% include w3api/param_description.html metodo=_dato parametro="KeyManager[] km" %}

## Excepciones
[KeyManagementException](/Java/KeyManagementException/)

## Clase Padre
[SSLContextSpi](/Java/SSLContextSpi/)

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
