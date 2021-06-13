---
title: NamespaceChangeListener
permalink: /Java/NamespaceChangeListener/
date: 2021-01-11
key: Java.N.NamespaceChangeListener
category: Java
tags: ['java se', 'javax.naming.event', 'java.naming', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.N.NamespaceChangeListener.description }}

## Sintaxis
~~~java
public interface NamespaceChangeListener extends NamingListener
~~~

## Métodos
* [objectAdded()](/Java/NamespaceChangeListener/objectAdded)
* [objectRemoved()](/Java/NamespaceChangeListener/objectRemoved)
* [objectRenamed()](/Java/NamespaceChangeListener/objectRenamed)

## Ejemplo
~~~java
{{ site.data.Java.N.NamespaceChangeListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NamespaceChangeListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
