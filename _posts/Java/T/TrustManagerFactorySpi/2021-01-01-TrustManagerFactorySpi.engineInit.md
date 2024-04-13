---
title: TrustManagerFactorySpi.engineInit()
permalink: /Java/TrustManagerFactorySpi/engineInit/
date: 2021-01-11
key: Java.T.TrustManagerFactorySpi
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TrustManagerFactorySpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(KeyStore ks) throws KeyStoreException
protected abstract void engineInit(ManagerFactoryParameters spec) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **ManagerFactoryParameters spec**,  {% include w3api/param_description.html metodo=_dato parametro="ManagerFactoryParameters spec" %}
* **KeyStore ks**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore ks" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [KeyStoreException](/Java/KeyStoreException/)

## Clase Padre
[TrustManagerFactorySpi](/Java/TrustManagerFactorySpi/)

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
