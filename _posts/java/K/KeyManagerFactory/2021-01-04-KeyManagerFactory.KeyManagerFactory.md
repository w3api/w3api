---
title: KeyManagerFactory.KeyManagerFactory()
permalink: Java/KeyManagerFactory/KeyManagerFactory
date: 2021-01-04
key: JavaJava.K.KeyManagerFactory
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyManagerFactory.constructores valor="KeyManagerFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected KeyManagerFactory(KeyManagerFactorySpi factorySpi, Provider provider, String algorithm)
~~~

## Parámetros
* **KeyManagerFactorySpi factorySpi**,  {% include w3api/param_description.html metodo=_data parametro="KeyManagerFactorySpi factorySpi" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}

## Clase Padre
[KeyManagerFactory](/Java/KeyManagerFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyManagerFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
