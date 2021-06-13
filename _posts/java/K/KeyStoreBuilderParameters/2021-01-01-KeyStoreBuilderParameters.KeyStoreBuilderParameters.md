---
title: KeyStoreBuilderParameters.KeyStoreBuilderParameters()
permalink: /Java/KeyStoreBuilderParameters/KeyStoreBuilderParameters/
date: 2021-01-11
key: Java.K.KeyStoreBuilderParameters
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreBuilderParameters.constructores valor="KeyStoreBuilderParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public KeyStoreBuilderParameters(KeyStore.Builder builder)
public KeyStoreBuilderParameters(List<KeyStore.Builder> parameters)
~~~

## Parámetros
* **List&lt;KeyStore.Builder&gt; parameters**,  {% include w3api/param_description.html metodo=_dato parametro="List<KeyStore.Builder> parameters" %}
* **KeyStore.Builder builder**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore.Builder builder" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[KeyStoreBuilderParameters](/Java/KeyStoreBuilderParameters/)

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
