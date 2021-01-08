---
title: SSLSocket.setEnabledCipherSuites()
permalink: Java/SSLSocket/setEnabledCipherSuites
date: 2021-01-04
key: JavaJava.S.SSLSocket
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSocket.metodos valor="setEnabledCipherSuites" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setEnabledCipherSuites(String[] suites)
~~~

## Parámetros
* **String[] suites**,  {% include w3api/param_description.html metodo=_data parametro="String[] suites" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLSocket](/Java/SSLSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
