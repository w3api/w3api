---
title: TrustManagerFactory.init()
permalink: /Java/TrustManagerFactory/init/
date: 2021-01-11
key: Java.T.TrustManagerFactory
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TrustManagerFactory.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void init(KeyStore ks) throws KeyStoreException
public final void init(ManagerFactoryParameters spec) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **ManagerFactoryParameters spec**,  {% include w3api/param_description.html metodo=_dato parametro="ManagerFactoryParameters spec" %}
* **KeyStore ks**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore ks" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [KeyStoreException](/Java/KeyStoreException/)

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
