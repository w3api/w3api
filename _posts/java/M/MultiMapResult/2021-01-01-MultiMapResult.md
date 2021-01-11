---
title: MultiMapResult
permalink: Java/MultiMapResult
date: 2021-01-11
key: JavaJava.M.MultiMapResult
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MultiMapResult.description }}

## Sintaxis
~~~java
public class MultiMapResult<V> extends Object implements Map<HttpRequest,CompletableFuture<HttpResponse<V>>>
~~~

## Ejemplo
~~~java
{{ site.data.Java.M.MultiMapResult.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MultiMapResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
