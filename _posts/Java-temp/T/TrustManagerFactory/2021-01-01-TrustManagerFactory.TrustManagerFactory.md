---
title: TrustManagerFactory.TrustManagerFactory()
permalink: /Java/TrustManagerFactory/TrustManagerFactory/
date: 2021-01-11
key: Java.T.TrustManagerFactory
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TrustManagerFactory.constructores valor="TrustManagerFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected TrustManagerFactory(TrustManagerFactorySpi factorySpi, Provider provider, String algorithm)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **TrustManagerFactorySpi factorySpi**,  {% include w3api/param_description.html metodo=_dato parametro="TrustManagerFactorySpi factorySpi" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}

## Clase Padre
[TrustManagerFactory](/Java/TrustManagerFactory/)

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
