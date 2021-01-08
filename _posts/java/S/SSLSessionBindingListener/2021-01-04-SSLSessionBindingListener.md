---
title: SSLSessionBindingListener
permalink: Java/SSLSessionBindingListener
date: 2021-01-04
key: JavaJava.S.SSLSessionBindingListener
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLSessionBindingListener.description }}

## Sintaxis
~~~java
public interface SSLSessionBindingListener extends EventListener
~~~

## Métodos
* [valueBound()](/Java/SSLSessionBindingListener/valueBound)
* [valueUnbound()](/Java/SSLSessionBindingListener/valueUnbound)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLSessionBindingListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLSessionBindingListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
