---
title: ConfirmationCallback
permalink: /Java/ConfirmationCallback/
date: 2021-01-11
key: Java.C.ConfirmationCallback
category: Java
tags: ['java se', 'javax.security.auth.callback', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConfirmationCallback.description }}

## Sintaxis
~~~java
public class ConfirmationCallback extends Object implements Callback, Serializable
~~~

## Constructores
* [ConfirmationCallback()](/Java/ConfirmationCallback/ConfirmationCallback/)

## Campos
* [CANCEL](/Java/ConfirmationCallback/CANCEL)
* [ERROR](/Java/ConfirmationCallback/ERROR)
* [INFORMATION](/Java/ConfirmationCallback/INFORMATION)
* [NO](/Java/ConfirmationCallback/NO)
* [OK](/Java/ConfirmationCallback/OK)
* [OK_CANCEL_OPTION](/Java/ConfirmationCallback/OK_CANCEL_OPTION)
* [UNSPECIFIED_OPTION](/Java/ConfirmationCallback/UNSPECIFIED_OPTION)
* [WARNING](/Java/ConfirmationCallback/WARNING)
* [YES](/Java/ConfirmationCallback/YES)
* [YES_NO_CANCEL_OPTION](/Java/ConfirmationCallback/YES_NO_CANCEL_OPTION)
* [YES_NO_OPTION](/Java/ConfirmationCallback/YES_NO_OPTION)

## Métodos
* [getDefaultOption()](/Java/ConfirmationCallback/getDefaultOption)
* [getMessageType()](/Java/ConfirmationCallback/getMessageType)
* [getOptions()](/Java/ConfirmationCallback/getOptions)
* [getOptionType()](/Java/ConfirmationCallback/getOptionType)
* [getPrompt()](/Java/ConfirmationCallback/getPrompt)
* [getSelectedIndex()](/Java/ConfirmationCallback/getSelectedIndex)
* [setSelectedIndex()](/Java/ConfirmationCallback/setSelectedIndex)

## Ejemplo
~~~java
{{ site.data.Java.C.ConfirmationCallback.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConfirmationCallback.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
