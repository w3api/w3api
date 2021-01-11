---
title: WebServiceProvider
permalink: Java/WebServiceProvider
date: 2021-01-11
key: JavaJava.W.WebServiceProvider
category: java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'anotacion java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebServiceProvider.description }}

## Sintaxis
~~~java
@Target(TYPE) @Retention(RUNTIME) @Documented public @interface WebServiceProvider
~~~

## Elementos
* [portName](/Java/WebServiceProvider/portName)
* [serviceName](/Java/WebServiceProvider/serviceName)
* [targetNamespace](/Java/WebServiceProvider/targetNamespace)
* [wsdlLocation](/Java/WebServiceProvider/wsdlLocation)

## Ejemplo
~~~java
{{ site.data.Java.W.WebServiceProvider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebServiceProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
