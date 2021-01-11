---
title: KeyStoreSpi.engineGetCertificateChain()
permalink: Java/KeyStoreSpi/engineGetCertificateChain
date: 2021-01-11
key: JavaJava.K.KeyStoreSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineGetCertificateChain" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Certificate[] engineGetCertificateChain(String alias)
~~~

## Parámetros
* **String alias**,  {% include w3api/param_description.html metodo=_dato parametro="String alias" %}

## Clase Padre
[KeyStoreSpi](/Java/KeyStoreSpi/)

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
