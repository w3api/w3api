---
title: SSLContext.SSLContext()
permalink: Java/SSLContext/SSLContext
date: 2021-01-04
key: JavaJava.S.SSLContext
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLContext.constructores valor="SSLContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SSLContext(SSLContextSpi contextSpi, Provider provider, String protocol)
~~~

## Parámetros
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}
* **SSLContextSpi contextSpi**,  {% include w3api/param_description.html metodo=_data parametro="SSLContextSpi contextSpi" %}

## Clase Padre
[SSLContext](/Java/SSLContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
