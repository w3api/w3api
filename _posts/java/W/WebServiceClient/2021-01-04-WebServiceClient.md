---
title: WebServiceClient
permalink: Java/WebServiceClient
date: 2021-01-04
key: JavaJava.W.WebServiceClient
category: java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'anotacion java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebServiceClient.description }}

## Sintaxis
~~~java
@Target(TYPE) @Retention(RUNTIME) @Documented public @interface WebServiceClient
~~~

## Elementos
* [name](/Java/WebServiceClient/name)
* [targetNamespace](/Java/WebServiceClient/targetNamespace)
* [wsdlLocation](/Java/WebServiceClient/wsdlLocation)

## Ejemplo
~~~java
{{ site.data.Java.W.WebServiceClient.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebServiceClient.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
