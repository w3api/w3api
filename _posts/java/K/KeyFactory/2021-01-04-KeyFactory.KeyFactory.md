---
title: KeyFactory.KeyFactory()
permalink: Java/KeyFactory/KeyFactory
date: 2021-01-04
key: JavaJava.K.KeyFactory
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyFactory.constructores valor="KeyFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected KeyFactory(KeyFactorySpi keyFacSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **KeyFactorySpi keyFacSpi**,  {% include w3api/param_description.html metodo=_data parametro="KeyFactorySpi keyFacSpi" %}

## Clase Padre
[KeyFactory](/Java/KeyFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
