---
title: SSLContextSpi.engineInit()
permalink: Java/SSLContextSpi/engineInit
date: 2021-01-04
key: JavaJava.S.SSLContextSpi
category: java
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
* **KeyManager[] km**,  {% include w3api/param_description.html metodo=_data parametro="KeyManager[] km" %}
* **SecureRandom sr**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandom sr" %}
* **TrustManager[] tm**,  {% include w3api/param_description.html metodo=_data parametro="TrustManager[] tm" %}

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
{%- for _ldc in site.data.Java.S.SSLContextSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
