---
title: SecretKeyFactory.SecretKeyFactory()
permalink: /Java/SecretKeyFactory/SecretKeyFactory/
date: 2021-01-11
key: Java.S.SecretKeyFactory
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecretKeyFactory.constructores valor="SecretKeyFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SecretKeyFactory(SecretKeyFactorySpi keyFacSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **SecretKeyFactorySpi keyFacSpi**,  {% include w3api/param_description.html metodo=_dato parametro="SecretKeyFactorySpi keyFacSpi" %}

## Clase Padre
[SecretKeyFactory](/Java/SecretKeyFactory/)

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
