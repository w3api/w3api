---
title: SSLEngine.setEnabledCipherSuites()
permalink: Java/SSLEngine/setEnabledCipherSuites
date: 2021-01-11
key: JavaJava.S.SSLEngine
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLEngine.metodos valor="setEnabledCipherSuites" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setEnabledCipherSuites(String[] suites)
~~~

## Parámetros
* **String[] suites**,  {% include w3api/param_description.html metodo=_dato parametro="String[] suites" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLEngine](/Java/SSLEngine/)

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
