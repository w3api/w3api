---
title: HostnameVerifier.verify()
permalink: /Java/HostnameVerifier/verify/
date: 2021-01-11
key: Java.H.HostnameVerifier
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HostnameVerifier.metodos valor="verify" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean verify(String hostname, SSLSession session)
~~~

## Parámetros
* **String hostname**,  {% include w3api/param_description.html metodo=_dato parametro="String hostname" %}
* **SSLSession session**,  {% include w3api/param_description.html metodo=_dato parametro="SSLSession session" %}

## Clase Padre
[HostnameVerifier](/Java/HostnameVerifier/)

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
