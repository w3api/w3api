---
title: WebService
permalink: Java/WebService
date: 2021-01-04
key: JavaJava.W.WebService
category: java
tags: ['java se', 'javax.jws', 'java.xml.ws', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebService.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(TYPE) public @interface WebService
~~~

## Elementos
* [endpointInterface](/Java/WebService/endpointInterface)
* [name](/Java/WebService/name)
* [portName](/Java/WebService/portName)
* [serviceName](/Java/WebService/serviceName)
* [targetNamespace](/Java/WebService/targetNamespace)
* [wsdlLocation](/Java/WebService/wsdlLocation)

## Ejemplo
~~~java
{{ site.data.Java.W.WebService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
