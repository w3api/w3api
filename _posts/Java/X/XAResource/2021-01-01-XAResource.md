---
title: XAResource
permalink: /Java/XAResource/
date: 2021-01-11
key: Java.X.XAResource
category: Java
tags: ['java se', 'javax.transaction.xa', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XAResource.description }}

## Sintaxis
~~~java
public interface XAResource
~~~

## Campos
* [TMENDRSCAN](/Java/XAResource/TMENDRSCAN/)
* [TMFAIL](/Java/XAResource/TMFAIL/)
* [TMJOIN](/Java/XAResource/TMJOIN/)
* [TMNOFLAGS](/Java/XAResource/TMNOFLAGS/)
* [TMONEPHASE](/Java/XAResource/TMONEPHASE/)
* [TMRESUME](/Java/XAResource/TMRESUME/)
* [TMSTARTRSCAN](/Java/XAResource/TMSTARTRSCAN/)
* [TMSUCCESS](/Java/XAResource/TMSUCCESS/)
* [TMSUSPEND](/Java/XAResource/TMSUSPEND/)
* [XA_OK](/Java/XAResource/XA_OK/)
* [XA_RDONLY](/Java/XAResource/XA_RDONLY/)

## Métodos
* [commit()](/Java/XAResource/commit/)
* [end()](/Java/XAResource/end/)
* [forget()](/Java/XAResource/forget/)
* [getTransactionTimeout()](/Java/XAResource/getTransactionTimeout/)
* [isSameRM()](/Java/XAResource/isSameRM/)
* [prepare()](/Java/XAResource/prepare/)
* [recover()](/Java/XAResource/recover/)
* [rollback()](/Java/XAResource/rollback/)
* [setTransactionTimeout()](/Java/XAResource/setTransactionTimeout/)
* [start()](/Java/XAResource/start/)

## Ejemplo
~~~java
{{ site.data.Java.X.XAResource.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XAResource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
