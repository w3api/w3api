---
title: TrustManagerFactorySpi.engineInit()
permalink: Java/TrustManagerFactorySpi/engineInit
date: 2021-01-04
key: JavaJava.T.TrustManagerFactorySpi
category: java
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
* **KeyStore ks**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore ks" %}
* **ManagerFactoryParameters spec**,  {% include w3api/param_description.html metodo=_data parametro="ManagerFactoryParameters spec" %}

## Excepciones
[KeyStoreException](/Java/KeyStoreException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[TrustManagerFactorySpi](/Java/TrustManagerFactorySpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TrustManagerFactorySpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
