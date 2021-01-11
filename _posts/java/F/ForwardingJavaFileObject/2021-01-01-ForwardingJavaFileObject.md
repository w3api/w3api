---
title: ForwardingJavaFileObject
permalink: Java/ForwardingJavaFileObject
date: 2021-01-11
key: JavaJava.F.ForwardingJavaFileObject
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.ForwardingJavaFileObject.description }}

## Sintaxis
~~~java
public class ForwardingJavaFileObject<F extends JavaFileObject> extends ForwardingFileObject<F> implements JavaFileObject
~~~

## Constructores
* [ForwardingJavaFileObject()](/Java/ForwardingJavaFileObject/ForwardingJavaFileObject/)

## Ejemplo
~~~java
{{ site.data.Java.F.ForwardingJavaFileObject.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForwardingJavaFileObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
